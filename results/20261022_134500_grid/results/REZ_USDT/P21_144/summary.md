# EMA Hourly Continuation — REZ/USDT P21_144

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.9066 |
| net_win_rate | 0.5371 |
| gross_profit_factor | 1.1649 |
| gross_win_rate | 0.5393 |
| sharpe_ratio | -0.6548 |
| sortino_ratio | -0.2031 |
| max_drawdown | 0.3300 |
| cagr | -0.0947 |
| net_avg_win | 86.0403 |
| net_avg_loss | -110.1288 |
| avg_hold_time_bars | 26.0087 |
| exposure | 0.5496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
