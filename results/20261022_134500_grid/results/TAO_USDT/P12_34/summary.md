# EMA Hourly Continuation — TAO/USDT P12_34

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1322 |
| net_profit_factor | 0.5541 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.9073 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -8.0601 |
| sortino_ratio | -4.1121 |
| max_drawdown | 0.9939 |
| cagr | -0.8673 |
| net_avg_win | 20.6136 |
| net_avg_loss | -30.8228 |
| avg_hold_time_bars | 3.7300 |
| exposure | 0.2241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
