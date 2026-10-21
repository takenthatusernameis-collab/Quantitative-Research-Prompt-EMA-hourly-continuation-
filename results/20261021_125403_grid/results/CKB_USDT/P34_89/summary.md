# EMA Hourly Continuation — CKB/USDT P34_89

**Symbol:** CKB/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.6785 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.8860 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -2.8028 |
| sortino_ratio | -0.8469 |
| max_drawdown | 0.6233 |
| cagr | -0.3221 |
| net_avg_win | 62.9372 |
| net_avg_loss | -80.4429 |
| avg_hold_time_bars | 10.2956 |
| exposure | 0.2106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
