# EMA Hourly Continuation — ONT/USDT P26_34

**Symbol:** ONT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1031 |
| net_profit_factor | 0.2517 |
| net_win_rate | 0.3424 |
| gross_profit_factor | 0.7166 |
| gross_win_rate | 0.3899 |
| sharpe_ratio | -13.6216 |
| sortino_ratio | -6.3782 |
| max_drawdown | 0.9998 |
| cagr | -0.9666 |
| net_avg_win | 9.5272 |
| net_avg_loss | -19.7068 |
| avg_hold_time_bars | 2.3191 |
| exposure | 0.1082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
