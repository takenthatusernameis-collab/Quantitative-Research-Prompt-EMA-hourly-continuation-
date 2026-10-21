# EMA Hourly Continuation — IMX/USDT P34_144

**Symbol:** IMX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8546 |
| net_win_rate | 0.5095 |
| gross_profit_factor | 1.0192 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -0.8017 |
| sortino_ratio | -0.2205 |
| max_drawdown | 0.3069 |
| cagr | -0.0991 |
| net_avg_win | 72.3767 |
| net_avg_loss | -87.9658 |
| avg_hold_time_bars | 24.7642 |
| exposure | 0.4135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
