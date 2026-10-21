# EMA Hourly Continuation — TIA/USDT P50_89

**Symbol:** TIA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8400 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0591 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -1.0144 |
| sortino_ratio | -0.2714 |
| max_drawdown | 0.2718 |
| cagr | -0.1187 |
| net_avg_win | 80.2021 |
| net_avg_loss | -101.1572 |
| avg_hold_time_bars | 7.4335 |
| exposure | 0.1169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
