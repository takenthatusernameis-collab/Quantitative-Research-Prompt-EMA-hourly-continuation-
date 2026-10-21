# EMA Hourly Continuation — DCR/USDT P8_89

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.7049 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.8909 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -2.3684 |
| sortino_ratio | -0.8228 |
| max_drawdown | 0.6348 |
| cagr | -0.3157 |
| net_avg_win | 51.0851 |
| net_avg_loss | -67.3310 |
| avg_hold_time_bars | 21.5151 |
| exposure | 0.5822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
