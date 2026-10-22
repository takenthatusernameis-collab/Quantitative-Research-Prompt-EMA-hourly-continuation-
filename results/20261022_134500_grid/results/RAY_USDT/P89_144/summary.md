# EMA Hourly Continuation — RAY/USDT P89_144

**Symbol:** RAY/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.5142 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8850 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -4.3959 |
| sortino_ratio | -1.3678 |
| max_drawdown | 0.8254 |
| cagr | -0.4866 |
| net_avg_win | 38.3945 |
| net_avg_loss | -62.8788 |
| avg_hold_time_bars | 5.4755 |
| exposure | 0.1220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
