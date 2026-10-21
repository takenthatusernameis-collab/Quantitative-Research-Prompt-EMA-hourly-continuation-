# EMA Hourly Continuation — KSM/USDT P89_144

**Symbol:** KSM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.7288 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0189 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -1.6236 |
| sortino_ratio | -0.3919 |
| max_drawdown | 0.4144 |
| cagr | -0.1643 |
| net_avg_win | 68.1820 |
| net_avg_loss | -96.2429 |
| avg_hold_time_bars | 6.8404 |
| exposure | 0.0877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
