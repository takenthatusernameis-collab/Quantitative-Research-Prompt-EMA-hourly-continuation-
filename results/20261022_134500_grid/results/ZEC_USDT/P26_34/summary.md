# EMA Hourly Continuation — ZEC/USDT P26_34

**Symbol:** ZEC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.2230 |
| net_win_rate | 0.4014 |
| gross_profit_factor | 0.7840 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -11.0183 |
| sortino_ratio | -4.9248 |
| max_drawdown | 0.9985 |
| cagr | -0.9256 |
| net_avg_win | 7.2562 |
| net_avg_loss | -21.8193 |
| avg_hold_time_bars | 2.0335 |
| exposure | 0.0910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
