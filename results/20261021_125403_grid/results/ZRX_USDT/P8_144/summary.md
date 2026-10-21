# EMA Hourly Continuation — ZRX/USDT P8_144

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.8477 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0331 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -0.9169 |
| sortino_ratio | -0.2483 |
| max_drawdown | 0.2979 |
| cagr | -0.1102 |
| net_avg_win | 77.2501 |
| net_avg_loss | -95.8466 |
| avg_hold_time_bars | 46.4818 |
| exposure | 0.7543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
