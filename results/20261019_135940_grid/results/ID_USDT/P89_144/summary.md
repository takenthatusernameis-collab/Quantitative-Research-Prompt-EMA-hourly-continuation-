# EMA Hourly Continuation — ID/USDT P89_144

**Symbol:** ID/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.4659 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.8244 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -4.5550 |
| sortino_ratio | -1.3412 |
| max_drawdown | 0.8142 |
| cagr | -0.4869 |
| net_avg_win | 35.5068 |
| net_avg_loss | -62.2164 |
| avg_hold_time_bars | 6.6090 |
| exposure | 0.1331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
