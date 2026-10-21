# EMA Hourly Continuation — DBR/USDT P55_89

**Symbol:** DBR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.5682 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -3.2099 |
| sortino_ratio | -0.7965 |
| max_drawdown | 0.5485 |
| cagr | -0.3077 |
| net_avg_win | 61.8741 |
| net_avg_loss | -92.2739 |
| avg_hold_time_bars | 8.7190 |
| exposure | 0.1200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
