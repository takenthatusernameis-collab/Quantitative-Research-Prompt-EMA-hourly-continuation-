# EMA Hourly Continuation — KCS/USDT P34_89

**Symbol:** KCS/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.1965 |
| net_win_rate | 0.3638 |
| gross_profit_factor | 0.6091 |
| gross_win_rate | 0.4023 |
| sharpe_ratio | -10.7724 |
| sortino_ratio | -4.1345 |
| max_drawdown | 0.9960 |
| cagr | -0.8884 |
| net_avg_win | 9.5531 |
| net_avg_loss | -27.7925 |
| avg_hold_time_bars | 7.8987 |
| exposure | 0.2517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
