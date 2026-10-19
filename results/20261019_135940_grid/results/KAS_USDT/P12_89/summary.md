# EMA Hourly Continuation — KAS/USDT P12_89

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.5321 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.8968 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -5.0316 |
| sortino_ratio | -1.9770 |
| max_drawdown | 0.9183 |
| cagr | -0.6242 |
| net_avg_win | 27.7294 |
| net_avg_loss | -46.3089 |
| avg_hold_time_bars | 14.4203 |
| exposure | 0.5224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
