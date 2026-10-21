# EMA Hourly Continuation — KAVA/USDT P12_55

**Symbol:** KAVA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.6958 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9692 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -3.7934 |
| sortino_ratio | -1.3997 |
| max_drawdown | 0.8252 |
| cagr | -0.4796 |
| net_avg_win | 58.1735 |
| net_avg_loss | -74.6531 |
| avg_hold_time_bars | 12.5565 |
| exposure | 0.3835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
