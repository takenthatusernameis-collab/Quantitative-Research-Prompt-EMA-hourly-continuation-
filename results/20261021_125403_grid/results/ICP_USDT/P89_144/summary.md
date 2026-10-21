# EMA Hourly Continuation — ICP/USDT P89_144

**Symbol:** ICP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.8600 |
| net_win_rate | 0.5372 |
| gross_profit_factor | 1.1425 |
| gross_win_rate | 0.5372 |
| sharpe_ratio | -0.6576 |
| sortino_ratio | -0.1480 |
| max_drawdown | 0.2020 |
| cagr | -0.0672 |
| net_avg_win | 75.8023 |
| net_avg_loss | -102.3063 |
| avg_hold_time_bars | 7.5785 |
| exposure | 0.0834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
