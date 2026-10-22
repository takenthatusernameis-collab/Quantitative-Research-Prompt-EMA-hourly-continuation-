# EMA Hourly Continuation — NYM/USDT P12_89

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.5741 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 0.7990 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -3.3105 |
| sortino_ratio | -0.9044 |
| max_drawdown | 0.6654 |
| cagr | -0.3411 |
| net_avg_win | 53.3703 |
| net_avg_loss | -73.2952 |
| avg_hold_time_bars | 34.2151 |
| exposure | 0.5785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
