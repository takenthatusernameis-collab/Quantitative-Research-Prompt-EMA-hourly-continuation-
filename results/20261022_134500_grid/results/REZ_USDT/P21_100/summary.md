# EMA Hourly Continuation — REZ/USDT P21_100

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.7682 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0393 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -2.0071 |
| sortino_ratio | -0.7144 |
| max_drawdown | 0.6284 |
| cagr | -0.2875 |
| net_avg_win | 59.1709 |
| net_avg_loss | -81.1028 |
| avg_hold_time_bars | 14.7742 |
| exposure | 0.4226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
