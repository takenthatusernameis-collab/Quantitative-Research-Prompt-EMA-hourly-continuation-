# EMA Hourly Continuation — ONE/USDT P20_89

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.8401 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0235 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -1.1879 |
| sortino_ratio | -0.3719 |
| max_drawdown | 0.3991 |
| cagr | -0.1592 |
| net_avg_win | 76.6802 |
| net_avg_loss | -93.9908 |
| avg_hold_time_bars | 18.6604 |
| exposure | 0.4046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
