# EMA Hourly Continuation — XEC/USDT P55_89

**Symbol:** XEC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.5503 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8288 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -3.4667 |
| sortino_ratio | -0.9994 |
| max_drawdown | 0.6898 |
| cagr | -0.3673 |
| net_avg_win | 44.5840 |
| net_avg_loss | -69.8666 |
| avg_hold_time_bars | 6.2266 |
| exposure | 0.1144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
