# EMA Hourly Continuation — MLK/USDT P12_89

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1020 |
| net_profit_factor | 0.3867 |
| net_win_rate | 0.3216 |
| gross_profit_factor | 0.6575 |
| gross_win_rate | 0.3304 |
| sharpe_ratio | -11.6661 |
| sortino_ratio | -5.2811 |
| max_drawdown | 0.9988 |
| cagr | -0.9287 |
| net_avg_win | 19.1960 |
| net_avg_loss | -23.5310 |
| avg_hold_time_bars | 10.5931 |
| exposure | 0.4890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
