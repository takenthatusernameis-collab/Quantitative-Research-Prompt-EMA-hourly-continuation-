# EMA Hourly Continuation — XAI/USDT P34_55

**Symbol:** XAI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6823 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.9256 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -2.6168 |
| sortino_ratio | -0.7567 |
| max_drawdown | 0.6193 |
| cagr | -0.2927 |
| net_avg_win | 63.9726 |
| net_avg_loss | -85.4368 |
| avg_hold_time_bars | 5.5746 |
| exposure | 0.1036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
