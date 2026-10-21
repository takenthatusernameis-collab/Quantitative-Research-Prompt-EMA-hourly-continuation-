# EMA Hourly Continuation — CTC/USDT P55_100

**Symbol:** CTC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.5965 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.8550 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -2.9031 |
| sortino_ratio | -0.7758 |
| max_drawdown | 0.6066 |
| cagr | -0.3003 |
| net_avg_win | 53.6850 |
| net_avg_loss | -78.4556 |
| avg_hold_time_bars | 9.0229 |
| exposure | 0.1435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
