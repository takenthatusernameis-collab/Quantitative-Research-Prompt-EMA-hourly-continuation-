# EMA Hourly Continuation — DBR/USDT P12_21

**Symbol:** DBR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.5738 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 1.0257 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -3.7020 |
| sortino_ratio | -1.0852 |
| max_drawdown | 0.6701 |
| cagr | -0.3935 |
| net_avg_win | 53.3025 |
| net_avg_loss | -84.9366 |
| avg_hold_time_bars | 6.6597 |
| exposure | 0.1269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
