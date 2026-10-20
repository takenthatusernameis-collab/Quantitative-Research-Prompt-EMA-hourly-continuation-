# EMA Hourly Continuation — ATH/USDT P26_34

**Symbol:** ATH/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.3204 |
| net_win_rate | 0.4065 |
| gross_profit_factor | 0.7727 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -11.0897 |
| sortino_ratio | -5.1838 |
| max_drawdown | 0.9984 |
| cagr | -0.9338 |
| net_avg_win | 11.4516 |
| net_avg_loss | -24.4831 |
| avg_hold_time_bars | 1.9753 |
| exposure | 0.0968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
