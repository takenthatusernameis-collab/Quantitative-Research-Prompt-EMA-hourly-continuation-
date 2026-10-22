# EMA Hourly Continuation — XDC/USDT P34_89

**Symbol:** XDC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 795 |
| net_profit_factor | 0.2601 |
| net_win_rate | 0.4277 |
| gross_profit_factor | 0.7050 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -8.9290 |
| sortino_ratio | -3.5217 |
| max_drawdown | 0.9919 |
| cagr | -0.8511 |
| net_avg_win | 10.2514 |
| net_avg_loss | -29.4543 |
| avg_hold_time_bars | 6.2717 |
| exposure | 0.2266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
