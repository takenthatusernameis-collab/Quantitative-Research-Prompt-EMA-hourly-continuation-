# EMA Hourly Continuation — ERG/USDT P20_34

**Symbol:** ERG/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.5143 |
| net_win_rate | 0.4128 |
| gross_profit_factor | 0.7285 |
| gross_win_rate | 0.4128 |
| sharpe_ratio | -3.7533 |
| sortino_ratio | -0.9207 |
| max_drawdown | 0.6681 |
| cagr | -0.3473 |
| net_avg_win | 56.6057 |
| net_avg_loss | -77.3584 |
| avg_hold_time_bars | 5.8557 |
| exposure | 0.0793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
