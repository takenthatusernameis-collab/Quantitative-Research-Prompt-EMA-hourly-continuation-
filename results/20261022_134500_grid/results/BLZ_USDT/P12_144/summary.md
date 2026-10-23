# EMA Hourly Continuation — BLZ/USDT P12_144

**Symbol:** BLZ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.6244 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8800 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -3.9940 |
| sortino_ratio | -1.3221 |
| max_drawdown | 0.8117 |
| cagr | -0.4706 |
| net_avg_win | 52.2963 |
| net_avg_loss | -68.6211 |
| avg_hold_time_bars | 25.7270 |
| exposure | 0.6567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
