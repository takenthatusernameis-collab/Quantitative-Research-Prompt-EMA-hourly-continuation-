# EMA Hourly Continuation — KAS/USDT P8_89

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.8922 |
| net_win_rate | 0.5260 |
| gross_profit_factor | 1.0961 |
| gross_win_rate | 0.5260 |
| sharpe_ratio | -0.7732 |
| sortino_ratio | -0.2536 |
| max_drawdown | 0.2891 |
| cagr | -0.1144 |
| net_avg_win | 79.7151 |
| net_avg_loss | -99.1544 |
| avg_hold_time_bars | 26.2524 |
| exposure | 0.6193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
