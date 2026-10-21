# EMA Hourly Continuation — YFI/USDT P8_55

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 778 |
| net_profit_factor | 0.6151 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.8924 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -3.8104 |
| sortino_ratio | -1.5167 |
| max_drawdown | 0.8280 |
| cagr | -0.5016 |
| net_avg_win | 35.2549 |
| net_avg_loss | -53.3351 |
| avg_hold_time_bars | 13.0604 |
| exposure | 0.4598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
