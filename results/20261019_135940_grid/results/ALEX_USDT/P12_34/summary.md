# EMA Hourly Continuation — ALEX/USDT P12_34

**Symbol:** ALEX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1118 |
| net_profit_factor | 0.4877 |
| net_win_rate | 0.3891 |
| gross_profit_factor | 0.8841 |
| gross_win_rate | 0.4088 |
| sharpe_ratio | -10.1386 |
| sortino_ratio | -4.7170 |
| max_drawdown | 0.9980 |
| cagr | -0.9156 |
| net_avg_win | 21.8393 |
| net_avg_loss | -28.5212 |
| avg_hold_time_bars | 5.2835 |
| exposure | 0.2685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
