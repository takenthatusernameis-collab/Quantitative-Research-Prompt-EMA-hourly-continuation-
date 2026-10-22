# EMA Hourly Continuation — PEPE/USDT P89_144

**Symbol:** PEPE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.5827 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9448 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -4.1835 |
| sortino_ratio | -1.3641 |
| max_drawdown | 0.8065 |
| cagr | -0.4781 |
| net_avg_win | 44.7727 |
| net_avg_loss | -69.8709 |
| avg_hold_time_bars | 4.6357 |
| exposure | 0.1110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
