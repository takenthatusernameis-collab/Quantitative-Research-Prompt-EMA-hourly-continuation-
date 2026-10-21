# EMA Hourly Continuation — DIA/USDT P12_21

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7266 |
| net_win_rate | 0.5232 |
| gross_profit_factor | 1.0838 |
| gross_win_rate | 0.5232 |
| sharpe_ratio | -2.1472 |
| sortino_ratio | -0.6737 |
| max_drawdown | 0.5496 |
| cagr | -0.2648 |
| net_avg_win | 57.8582 |
| net_avg_loss | -87.3766 |
| avg_hold_time_bars | 4.5970 |
| exposure | 0.0986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
