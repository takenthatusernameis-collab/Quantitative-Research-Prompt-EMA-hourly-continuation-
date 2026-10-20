# EMA Hourly Continuation — CHR/USDT P26_144

**Symbol:** CHR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.6713 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.8966 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -2.9216 |
| sortino_ratio | -0.9274 |
| max_drawdown | 0.6792 |
| cagr | -0.3502 |
| net_avg_win | 57.6113 |
| net_avg_loss | -75.2554 |
| avg_hold_time_bars | 21.5885 |
| exposure | 0.4914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
