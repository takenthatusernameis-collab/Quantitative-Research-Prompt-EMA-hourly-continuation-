# EMA Hourly Continuation — DIA/USDT P26_34

**Symbol:** DIA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1023 |
| net_profit_factor | 0.2289 |
| net_win_rate | 0.3969 |
| gross_profit_factor | 0.6617 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -11.1823 |
| sortino_ratio | -5.1143 |
| max_drawdown | 0.9986 |
| cagr | -0.9262 |
| net_avg_win | 7.3002 |
| net_avg_loss | -20.9886 |
| avg_hold_time_bars | 2.6188 |
| exposure | 0.1212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
