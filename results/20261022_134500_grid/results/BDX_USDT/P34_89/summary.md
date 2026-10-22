# EMA Hourly Continuation — BDX/USDT P34_89

**Symbol:** BDX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1206 |
| net_profit_factor | 0.2435 |
| net_win_rate | 0.2844 |
| gross_profit_factor | 0.6151 |
| gross_win_rate | 0.3425 |
| sharpe_ratio | -17.9109 |
| sortino_ratio | -9.3764 |
| max_drawdown | 1.0000 |
| cagr | -0.9946 |
| net_avg_win | 9.3835 |
| net_avg_loss | -15.3170 |
| avg_hold_time_bars | 3.7952 |
| exposure | 0.2080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
