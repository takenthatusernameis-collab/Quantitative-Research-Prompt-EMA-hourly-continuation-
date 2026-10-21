# EMA Hourly Continuation — IMX/USDT P50_55

**Symbol:** IMX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 117 |
| net_profit_factor | 1.2990 |
| net_win_rate | 0.6410 |
| gross_profit_factor | 1.7885 |
| gross_win_rate | 0.6410 |
| sharpe_ratio | 0.8635 |
| sortino_ratio | 0.1400 |
| max_drawdown | 0.0960 |
| cagr | 0.0572 |
| net_avg_win | 87.3073 |
| net_avg_loss | -120.0206 |
| avg_hold_time_bars | 4.3504 |
| exposure | 0.0230 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
