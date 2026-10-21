# EMA Hourly Continuation — ONE/USDT P8_144

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.9671 |
| net_win_rate | 0.5315 |
| gross_profit_factor | 1.1216 |
| gross_win_rate | 0.5315 |
| sharpe_ratio | -0.1586 |
| sortino_ratio | -0.0417 |
| max_drawdown | 0.2942 |
| cagr | -0.0246 |
| net_avg_win | 100.7656 |
| net_avg_loss | -118.2192 |
| avg_hold_time_bars | 51.2733 |
| exposure | 0.7761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
