# EMA Hourly Continuation — KNC/USDT P26_89

**Symbol:** KNC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.7542 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0449 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -2.3386 |
| sortino_ratio | -0.7435 |
| max_drawdown | 0.6514 |
| cagr | -0.2889 |
| net_avg_win | 71.7716 |
| net_avg_loss | -95.1566 |
| avg_hold_time_bars | 14.5935 |
| exposure | 0.3264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
