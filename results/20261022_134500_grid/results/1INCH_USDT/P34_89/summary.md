# EMA Hourly Continuation — 1INCH/USDT P34_89

**Symbol:** 1INCH/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.5152 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.9069 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -5.6498 |
| sortino_ratio | -2.1243 |
| max_drawdown | 0.9274 |
| cagr | -0.6433 |
| net_avg_win | 29.6999 |
| net_avg_loss | -50.0771 |
| avg_hold_time_bars | 8.4747 |
| exposure | 0.2743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
