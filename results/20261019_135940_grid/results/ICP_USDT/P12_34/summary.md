# EMA Hourly Continuation — ICP/USDT P12_34

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1331 |
| net_profit_factor | 0.4596 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8950 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -9.7323 |
| sortino_ratio | -4.9769 |
| max_drawdown | 0.9983 |
| cagr | -0.9195 |
| net_avg_win | 14.4605 |
| net_avg_loss | -24.8259 |
| avg_hold_time_bars | 3.5680 |
| exposure | 0.2159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
