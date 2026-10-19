# EMA Hourly Continuation — KMNO/USDT P50_100

**Symbol:** KMNO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.5520 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8731 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -4.5384 |
| sortino_ratio | -1.5139 |
| max_drawdown | 0.8365 |
| cagr | -0.5193 |
| net_avg_win | 41.0673 |
| net_avg_loss | -61.2229 |
| avg_hold_time_bars | 6.9353 |
| exposure | 0.1780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
