# EMA Hourly Continuation — ONE/USDT P89_144

**Symbol:** ONE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.5467 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.9104 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -4.6062 |
| sortino_ratio | -1.4733 |
| max_drawdown | 0.8376 |
| cagr | -0.5051 |
| net_avg_win | 43.6687 |
| net_avg_loss | -64.6320 |
| avg_hold_time_bars | 5.2793 |
| exposure | 0.1229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
