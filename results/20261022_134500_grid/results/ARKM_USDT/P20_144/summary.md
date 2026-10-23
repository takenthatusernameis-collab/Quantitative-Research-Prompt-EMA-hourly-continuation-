# EMA Hourly Continuation — ARKM/USDT P20_144

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.6210 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8426 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -3.4280 |
| sortino_ratio | -1.0735 |
| max_drawdown | 0.7245 |
| cagr | -0.3973 |
| net_avg_win | 53.3608 |
| net_avg_loss | -69.3036 |
| avg_hold_time_bars | 24.6182 |
| exposure | 0.5539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
