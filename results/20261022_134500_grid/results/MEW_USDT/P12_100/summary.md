# EMA Hourly Continuation — MEW/USDT P12_100

**Symbol:** MEW/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.5843 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8199 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -4.3874 |
| sortino_ratio | -1.5798 |
| max_drawdown | 0.8623 |
| cagr | -0.5335 |
| net_avg_win | 40.0817 |
| net_avg_loss | -56.5042 |
| avg_hold_time_bars | 19.0876 |
| exposure | 0.5744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
