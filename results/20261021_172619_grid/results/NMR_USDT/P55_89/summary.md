# EMA Hourly Continuation — NMR/USDT P55_89

**Symbol:** NMR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7317 |
| net_win_rate | 0.5141 |
| gross_profit_factor | 1.0473 |
| gross_win_rate | 0.5141 |
| sharpe_ratio | -1.8154 |
| sortino_ratio | -0.4920 |
| max_drawdown | 0.4507 |
| cagr | -0.2012 |
| net_avg_win | 64.6029 |
| net_avg_loss | -93.4251 |
| avg_hold_time_bars | 6.4520 |
| exposure | 0.1038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
