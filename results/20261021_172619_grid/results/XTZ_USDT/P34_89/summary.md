# EMA Hourly Continuation — XTZ/USDT P34_89

**Symbol:** XTZ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7044 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9821 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -2.5839 |
| sortino_ratio | -0.8103 |
| max_drawdown | 0.6144 |
| cagr | -0.3097 |
| net_avg_win | 61.6862 |
| net_avg_loss | -83.9824 |
| avg_hold_time_bars | 11.0669 |
| exposure | 0.2405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
