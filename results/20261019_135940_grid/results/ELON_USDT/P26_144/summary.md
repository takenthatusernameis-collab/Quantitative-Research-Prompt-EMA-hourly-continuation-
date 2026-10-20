# EMA Hourly Continuation — ELON/USDT P26_144

**Symbol:** ELON/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.5661 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.8144 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -4.3304 |
| sortino_ratio | -1.3923 |
| max_drawdown | 0.8097 |
| cagr | -0.4791 |
| net_avg_win | 46.5036 |
| net_avg_loss | -64.4651 |
| avg_hold_time_bars | 18.8288 |
| exposure | 0.4399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
