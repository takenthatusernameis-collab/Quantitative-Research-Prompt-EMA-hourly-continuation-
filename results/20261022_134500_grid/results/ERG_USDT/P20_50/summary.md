# EMA Hourly Continuation — ERG/USDT P20_50

**Symbol:** ERG/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1029 |
| net_profit_factor | 0.3109 |
| net_win_rate | 0.3722 |
| gross_profit_factor | 0.5897 |
| gross_win_rate | 0.3887 |
| sharpe_ratio | -10.7597 |
| sortino_ratio | -4.9076 |
| max_drawdown | 0.9980 |
| cagr | -0.9148 |
| net_avg_win | 11.7550 |
| net_avg_loss | -22.4173 |
| avg_hold_time_bars | 4.7833 |
| exposure | 0.2237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
