# EMA Hourly Continuation — CERE/USDT P34_89

**Symbol:** CERE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.4506 |
| net_win_rate | 0.3402 |
| gross_profit_factor | 0.8322 |
| gross_win_rate | 0.3687 |
| sharpe_ratio | -10.6063 |
| sortino_ratio | -4.2064 |
| max_drawdown | 0.9964 |
| cagr | -0.8903 |
| net_avg_win | 31.0601 |
| net_avg_loss | -35.5489 |
| avg_hold_time_bars | 8.1617 |
| exposure | 0.2868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
