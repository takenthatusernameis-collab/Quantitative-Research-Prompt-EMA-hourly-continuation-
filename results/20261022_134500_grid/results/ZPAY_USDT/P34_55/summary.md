# EMA Hourly Continuation — ZPAY/USDT P34_55

**Symbol:** ZPAY/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.3720 |
| net_win_rate | 0.3239 |
| gross_profit_factor | 0.6156 |
| gross_win_rate | 0.3303 |
| sharpe_ratio | -9.1354 |
| sortino_ratio | -3.5511 |
| max_drawdown | 0.9878 |
| cagr | -0.8228 |
| net_avg_win | 23.2955 |
| net_avg_loss | -30.0002 |
| avg_hold_time_bars | 6.9819 |
| exposure | 0.2449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
