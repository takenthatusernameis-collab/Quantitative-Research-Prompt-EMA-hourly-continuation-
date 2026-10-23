# EMA Hourly Continuation — METIS/USDT P8_89

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.6319 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.9034 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -4.2171 |
| sortino_ratio | -1.5351 |
| max_drawdown | 0.8432 |
| cagr | -0.5212 |
| net_avg_win | 46.8142 |
| net_avg_loss | -63.0636 |
| avg_hold_time_bars | 21.2857 |
| exposure | 0.6502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
