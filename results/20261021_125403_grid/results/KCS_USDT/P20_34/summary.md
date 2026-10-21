# EMA Hourly Continuation — KCS/USDT P20_34

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.3016 |
| net_win_rate | 0.3718 |
| gross_profit_factor | 0.6597 |
| gross_win_rate | 0.3846 |
| sharpe_ratio | -6.2530 |
| sortino_ratio | -1.6158 |
| max_drawdown | 0.8550 |
| cagr | -0.5349 |
| net_avg_win | 31.7857 |
| net_avg_loss | -62.3711 |
| avg_hold_time_bars | 6.7724 |
| exposure | 0.0960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
