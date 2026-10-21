# EMA Hourly Continuation — CRV/USDT P55_200

**Symbol:** CRV/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.7611 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9308 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -1.5347 |
| sortino_ratio | -0.3946 |
| max_drawdown | 0.4035 |
| cagr | -0.1665 |
| net_avg_win | 74.4874 |
| net_avg_loss | -91.4541 |
| avg_hold_time_bars | 19.2769 |
| exposure | 0.2848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
